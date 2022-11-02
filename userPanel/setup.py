import os,uuid

def handle_JPEG_image_file(f,exten):
    st = str(uuid.uuid4())
    with open('userPanel/static/userPanel/files/JPEG/'+st+"."+exten, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            viewPath = '/static/userPanel/files/JPEG/'+st+"."+exten
        return viewPath

def handle_PNG_image_file(f,exten):
    st = str(uuid.uuid4())
    with open('userPanel/static/userPanel/files/PNG/'+st+"."+exten, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            viewPath = '/static/userPanel/files/PNG/'+st+"."+exten
        return viewPath

def handle_JPG_image_file(f,exten):
    st = str(uuid.uuid4())
    with open('userPanel/static/userPanel/files/JPG/'+st+"."+exten, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            viewPath = '/static/userPanel/files/JPG/'+st+"."+exten
        return viewPath

def handle_AUDIO_file(f,exten):
    st = str(uuid.uuid4())
    with open('userPanel/static/userPanel/files/AUDIO/'+st+"."+exten, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            viewPath ='/static/userPanel/files/AUDIO/'+st+"."+exten
        return viewPath

def handle_VIDEO_file(f,exten):
    st = str(uuid.uuid4())
    with open('userPanel/static/userPanel/files/VIDEO/'+st+"."+exten,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            viewPath = '/static/userPanel/files/VIDEO/'+st+"."+exten
        return viewPath

def handle_STRANGE_file(f,exten):
    st = str(uuid.uuid4())
    with open('userPanel/static/userPanel/files/STRANGE/'+st+"."+exten,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            viewPath = '/static/userPanel/files/STRANGE/'+st+"."+exten
        return viewPath

def parmanent_file(f,exten):
    st = str(uuid.uuid4())
    with open('viewPanel/static/viewPanel/files/all_feature/' + st + "." + exten, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            viewPath = '/static/viewPanel/files/all_feature/' + st + "." + exten
        return viewPath

def extention(file):
    txt = file.name
    ext = txt.split(".")
    exten = ((ext[-1]).strip()).lower()
    return exten

def file_save(file,exten):

    if exten == 'jpg':
        path = handle_JPG_image_file(file,exten)
        return path
    elif exten == 'jpeg':
        path = handle_JPEG_image_file(file,exten)
        return path
    elif exten == 'png':
        path = handle_PNG_image_file(file,exten)
        return path
    elif exten == 'mp3':
        path = handle_AUDIO_file(file,exten)
        return path
    elif exten == 'mp4':
        path = handle_VIDEO_file(file,exten)
        return path
    else:
        path = handle_STRANGE_file(file, exten)
        return path


