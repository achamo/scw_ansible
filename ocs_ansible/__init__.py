import os
import json
import argparse
from ocs_sdk.apis import ComputeAPI

class OcsAnsible(object):

  def __init__(self):
    args = self.parse_args()

    hostgroups = { '_meta': { 'hostvars': {} } }

    if args.host != None:
      print json.dumps({})
    else:
      api = ComputeAPI(auth_token=os.environ['OCS_TOKEN'])
      hostgroups = { '_meta': { 'hostvars': {} } }
      for server in api.query().servers.get()['servers']:
        if server.get('state') != 'running':
          continue
        var = {}
        environments = []
        for tag in server.get('tags'):
          if tag.find(':') == -1:
            continue
          (key, value) = tag.split(':', 1)
          if key == 'environment':
            environments.append(value)
          else:
            var[key] = value
        for env in environments:
          if env not in hostgroups:
            hostgroups[env] = { 'hosts': [] }
          hostgroups[env]['hosts'].append(server.get('public_ip').get('address'))
        hostgroups['_meta']['hostvars'][server.get('public_ip').get('address')] = var

    if args.list == True:
      print json.dumps(hostgroups)

    if args.cssh == True:
      for group, values in hostgroups.iteritems():
        if group == '_meta':
          continue
        list_hosts = ["root@{0}".format(host) for host in values['hosts']]
        print "{0} = {1}".format(group, " ".join(list_hosts))

  def parse_args(self):
    parser = argparse.ArgumentParser(description="OCS inventory")
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--cssh', action='store_true')
    parser.add_argument('--host')
    return parser.parse_args()


def main():
  OcsAnsible()
