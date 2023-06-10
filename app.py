import dropbox
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


class DropboxAPI:
    def __init__(self, access_token):
        self.access_token = access_token
        self.client = dropbox.Dropbox(access_token)

    def list_files(self):
        files = self.client.files_list_folder("").entries
        return files

    def upload_file(self, file_path, file_name):
        with open(file_path, "rb") as file:
            self.client.files_upload(file.read(), f"/{file_name}")

    def download_file(self, file_path):
        _, file = self.client.files_download(file_path)
        return file.content

    def share_file(self, file_path):
        share_link = self.client.sharing_create_shared_link(file_path).url
        return share_link


@app.route("/")
def index():
    return redirect(url_for("list_files"))


@app.route("/list_files")
def list_files():
    dbx = DropboxAPI(
        "YOUR_DROPBOX_ACCESS_TOKEN")
    files = dbx.list_files()
    return render_template("list_files.html", files=files)


@app.route("/upload_file", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        file.save(file.filename)
        dbx = DropboxAPI(
            "YOUR_DROPBOX_ACCESS_TOKEN")
        dbx.upload_file(file.filename, file.filename)
        return redirect(url_for("list_files"))
    return render_template("upload_file.html")


@app.route("/download_file/<path:file_path>")
def download_file(file_path):
    # Add a leading forward slash to the file path
    if not file_path.startswith("/"):
        file_path = "/" + file_path

    dbx = DropboxAPI(
        "YOUR_DROPBOX_ACCESS_TOKEN")
    file_content = dbx.download_file(file_path)
    return file_content


@app.route("/share_file/<path:file_path>")
def share_file(file_path):
    # Add a leading forward slash to the file path
    if not file_path.startswith("/"):
        file_path = "/" + file_path

    dbx = dropbox.Dropbox(
        "YOUR_DROPBOX_ACCESS_TOKEN")
    try:
        shared_link = dbx.sharing_create_shared_link_with_settings(file_path)
        return redirect(shared_link.url)
    except dropbox.exceptions.ApiError as e:
        if isinstance(e.error, dropbox.sharing.SharedLinkAlreadyExistsError):
            shared_link = dbx.sharing_list_shared_links(file_path).links[0]
            return redirect(shared_link.url)
        else:
            return "Error creating shared link for the file."


if __name__ == "__main__":
    app.run(debug=True)
