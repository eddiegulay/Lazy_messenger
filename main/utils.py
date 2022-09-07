def profile_uploader(u, f):
    with open(f'lazy_media/profile_uploads/{u.username}_{f.name}', 'wb+') as destination:
        for chunk in f.chunks(): 
            destination.write(chunk)
            
    return f'profile_uploads/{u.username}_{f.name}'

def image_uploader(f):
    with open(f'lazy_media/image_uploads/lazy_uploded_{f.name}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return f'image_uploads/lazy_uploded_{f.name}'

def video_uploader(f):
    with open(f'lazy_media/video_uploads/lazy_uploded_{f.name}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            
    return f'video_uploads/lazy_uploded_{f.name}'