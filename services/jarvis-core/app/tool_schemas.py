TOOL_SCHEMAS = {
    'filesystem_read': {'type':'object','properties':{'path':{'type':'string'}},'required':['path'],'additionalProperties':False},
    'git_status': {'type':'object','properties':{},'additionalProperties':False},
    'git_diff': {'type':'object','properties':{'cached':{'type':'boolean'}},'additionalProperties':False},
    'test_runner': {'type':'object','properties':{'command':{'type':'string'}},'required':['command'],'additionalProperties':False},
    'build_runner': {'type':'object','properties':{'command':{'type':'string'}},'required':['command'],'additionalProperties':False},
    'docker_status': {'type':'object','properties':{},'additionalProperties':False},
}
