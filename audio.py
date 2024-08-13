import vertexai
from vertexai.generative_models import GenerativeModel, Part

project_id = "PROJECT_ID" # 書き換える

vertexai.init(project=project_id, location="asia-northeast1")

model = GenerativeModel("gemini-1.5-flash-001")
# model = GenerativeModel("gemini-1.5-pro-001")

audio_file_uri = "gs://bucket/filename.mp3" # 書き換える

audio_file = Part.from_uri(audio_file_uri, mime_type="audio/mpeg")

prompt = """
音声を日本語でテキストに変換してください
"""

contents = [audio_file, prompt]

response = model.generate_content(contents)

transcript = response.text

print(transcript)
