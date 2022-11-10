from django.shortcuts import render
import requests


def index(request):

    username = request.GET.get('username', 'askshar')

    url = f"https://api.github.com/users/{username}"
    repo_url = f"https://api.github.com/users/{username}/repos"
    data = requests.get(url).json()
    repo_data = requests.get(repo_url).json()

    # print("TOTAL REPO:", repo_data)
    count = 0

    for repo in repo_data:
        if "name" in repo:
            count+=1
            
    payload = {
        'username': data['login'],
        'name': data['name'],
        'bio': data['bio'],
        'followers': data['followers'],
        'following': data['following'],
        'avatar': data['avatar_url']
    }

    context = {
        'data': payload,
        'repos': count
    }

    return render(request, 'index.html', context)