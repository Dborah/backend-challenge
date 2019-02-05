import requests


class RoomsConsumerAPI:

    def __init__(self):
        self.requests = requests
        self.endpoint = 'http://127.0.0.1:5000/api/v1/rooms'

    def rooms_get(self):
        resp = self.requests.get(self.endpoint)
        return resp

    def room_get_item(self, room_id):
        resp = self.requests.get(f"{self.endpoint}/{room_id}")
        return resp

    def room_post(self, content):
        resp = self.requests.post(f"{self.endpoint}", json=content)
        return resp

    def room_update(self, room_id, content):
        resp = self.requests.put(f"{self.endpoint}/{room_id}", json=content)
        return resp

    def room_delete(self, room_id):
        resp = self.requests.delete(f"{self.endpoint}/{room_id}")
        return resp


if __name__ == '__main__':
    r = RoomsConsumerAPI()
    get_all = r.rooms_get()
    print("GET Room")
    print(get_all.status_code)
    print(get_all.url)
    print(get_all.headers)
    print(get_all.json())
    print()

    print("GET Room Item")
    get_item = r.room_get_item(2)
    print(get_item.status_code)
    print(get_item.url)
    print(get_item.headers)
    print(get_item.json())
    print()

    print("PUT Room")
    data = {
        'room_number': 100
    }
    resp_up = r.room_update(2, data)
    print(resp_up.status_code)
    print(resp_up.url)
    print(resp_up.headers)
    print(resp_up.json())
    print()

    # print("POST Room")
    # data = {
    #     'room_number': 96
    # }
    # resp_post = r.room_post(data)
    # print(resp_post.status_code)
    # print(resp_post.url)
    # print(resp_post.headers)
    # print(resp_post.json())
    # print()

    print("DELETE Room")
    resp_del = r.room_delete(1)
    print(resp_del.status_code)
    print(resp_del.url)
    print(resp_del.headers)
    print(resp_del.json())
