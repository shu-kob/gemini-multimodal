import vertexai
from vertexai.generative_models import GenerativeModel, Part

project_id = "PROJECT_ID" # 書き換える
vertexai.init(project=project_id, location="asia-northeast1")

model = GenerativeModel(model_name="gemini-1.5-flash-001")
# model = GenerativeModel(model_name="gemini-1.5-pro-001")

video_file_uri = "gs://bucket/filename.mp4" # 書き換える
video_file = Part.from_uri(video_file_uri, mime_type="video/mp4")

prompt = """
  この動画は何ですか？
"""

contents = [
    video_file,
    prompt,
]

response = model.generate_content(contents)
print(response.text)
