# Ruta con 2 parametros. Usuario y contraseña
# Desencriptar contraseña
# Retonar respuesta exitosa. Mensaje de no logueo 

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

@csrf_exempt
def login_view(request, username, password):
    # Imprimir los valores recibidos
    print(f"Received username: {username}")
    print(f"Received password: {password}")
    
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        response = {'status': 'success', 'message': 'Logged in successfully'}
    else:
        response = {'status': 'failure', 'message': 'Invalid username or password'}
    
    # Imprimir la respuesta que se va a devolver
    print(f"Response: {response}")
    
    return JsonResponse(response)


@api_view(['POST'])
def upload_image(request):
    # Probar ambas claves
    files_images = request.FILES.getlist('images')
    files_image = request.FILES.getlist('image')

    # Usar la clave que tiene archivos
    files = files_images if files_images else files_image

    # Print the received files
    print("Received files:", files)

    if not files:
        return Response({"message": "No files received"}, status=status.HTTP_400_BAD_REQUEST)

    for file in files:
        try:
            path = default_storage.save(f'productos/{file.name}', ContentFile(file.read()))
            # Print the saved file path
            print(f"File saved at: {path}")
        except Exception as e:
            return Response({"message": f"Error uploading file {file.name}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({"message": "Images uploaded successfully"}, status=status.HTTP_201_CREATED)




@api_view(['POST'])
def upload_image_users(request):
    files_image = request.FILES.getlist('image')

    if not files_image:
        return Response({"message": "No files received"}, status=status.HTTP_400_BAD_REQUEST)

    file = files_image[0]
    try:
        print(f"Received file: {file.name}")
        path = default_storage.save(f'usuarios/{file.name}', ContentFile(file.read()))
        file_url = default_storage.url(path)
        print(f"File saved at: {file_url}")
        return Response({"url": file_url, "message": "Image uploaded successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(f"Error uploading file {file.name}: {str(e)}")
        return Response({"message": f"Error uploading file {file.name}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)