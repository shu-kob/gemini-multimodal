import vertexai
from vertexai.generative_models import GenerativeModel, Part

project_id = "PROJECT_ID" # 書き換える
vertexai.init(project=project_id, location="asia-northeast1")

model = GenerativeModel(model_name="gemini-1.5-flash-001")

image_file_uri = "gs://bucket/filename.png" # 書き換える
image_file = Part.from_uri(image_file_uri, mime_type="image/png")

prompt = """
  この画像は何ですか？
"""

contents = [
    image_file,
    prompt,
]

response = model.generate_content(contents)
print(response.text)
