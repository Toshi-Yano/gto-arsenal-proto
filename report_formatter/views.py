import io

from .forms import FileUploadForm
import pandas as pd
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView


class FileUploadView(FormView):
    template_name = "report_formatter/upload.html"
    form_class = FileUploadForm
    success_url = reverse_lazy("file-upload")

    def form_valid(self, form):
        # フォームから受け取ったデータをデータフレームへ変換
        # ファイル形式に応じた読み込み
        file = io.TextIOWrapper(form.cleaned_data["file"])
        df = pd.read_csv(file, dtype=str, header=3)

        print(df.head(20))

        # ファイルの保存とダウンロード処理
        f_name = "new_filename"  # 日本語は使えない
        # ファイル形式に応じた保存とダウンロード処理
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename ="' + f_name + '.csv"'
        df.to_csv(path_or_buf=response, sep=",", index=False, encoding="utf-8")

        return response
