# _*_ coding: utf-8 _*_

from collections import deque

graph = {}
graph['you'] = ['alices', 'bobs', 'claires']
graph['bobs'] = ['anujs', 'peggys']
graph['alices'] = ['peggys']
graph['claires'] = ['thoms', 'jonnys', 'jack']
graph['anujs'] = []
graph['peggys'] = []
graph['thoms'] = []
graph['jonnys'] = []
graph['jack'] = ['lucy', 'mango_andrew']
graph['lucy'] = []
graph['mango_andrew'] = []


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()

        if person not in searched:
            if 'mango' in person:
                print(person[6:] + ' is a mongo seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    print('Not find mango seller')
    return False


search('you')
