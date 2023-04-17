import os
import csv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Slack APIトークン
token=os.environ['SLACK_API_TOKEN']='xoxp-5112729809968-5089040446195-5118144732163-74f6280b27f78c7daf9cca26251bd84b'
client = WebClient(token=os.environ['SLACK_API_TOKEN'])

# 全メンバー一覧を取得
try:
    response = client.users_list()
    members = response['members']
except SlackApiError as e:
    print("Error : {}".format(e))

# メンバーのアクティブ状態と名前を取得し、CSVファイルに書き込む
with open('active_members.csv', mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Member ID', 'Name', 'Active Time'])
    for member in members:
        try:
            response = client.users_getPresence(user=member['id'])
            active_time = response['presence']
            writer.writerow([member['id'], member['name'], active_time])
        except SlackApiError as e:
            print("Error : {}".format(e))

