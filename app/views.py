from django.shortcuts import render
import six, os
from google.cloud import language
from google.cloud.language import enums, types
from google_images_download import google_images_download

def home(request):
    return render(request, 'min1/home.html')

def index(request):

#     return render(request, 'app/index.html')

# def test(request):

#     return render (request, 'app/test.html')


# ########## Function ##########

# ##### Keyword extract module #####
# def init_entities(text):
#     # Preprocessing: Encoding
#     if isinstance(text, six.binary_type):
#         text = text.decode('utf-8')

#     # Instantiates a plain text document.
#     document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)

#     # Detects entities in the document
#     entities = client.analyze_entities(document).entities

#     if len(entities) == 0:
#         print("Keyword None\n Exit")
#         exit()
#     else:
#         print(entities[0].name)
#         return entities[0].name


# ##### Google image downloade module #####
# def download_images(query):
#     # Set arguments
#     arguments = {
#         "keywords": query,
#         "limit": 1,
#         "print_urls": True,
#         "size": "medium",
#         "output_directory": "C:/Users/david/Desktop/부엉이/teamproject/project/static/img", # 절대경로로 수정하세요.
#         "no_directory": True,
#     }
#     try:
#         response.download(arguments)
#     except FileNotFoundError:
#         arguments = {"keywords": query,
#                      "format": "jpg",
#                      "limit": 1,
#                      "print_urls": True,
#                      "size": "medium"
#                      }
#         try:
#             response.download(arguments)
#         except:
#             pass

# ########## Function ##########

# # User Authentication
# #credential_path = "파일이름.json"
# credential_path = "C:/Users/david/Desktop/부엉이/teamproject/app/handle8ton-a089bd5358fe.json"
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# # Instantiates Client
# client = language.LanguageServiceClient()

# # Instantiates downloader
# response = google_images_download.googleimagesdownload()

# # Analysing Entities in Text

# text = '저희 동네앞 쓰레기장 건설에 반대합니다.'

# # download_images(init_entities(str 변수입력))
# download_images(init_entities(text))

    return render(request, 'min1/index.html')    

def write(request):
    return render(request, 'min1/write.html')

def detail(request):
    return render(request, 'min1/detail.html')

def reported(request):
    return render(request, 'min1/reported.html')
