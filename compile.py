import yaml

def writeGroup(data, key):
    contact = data["groups"][key]["contact"]
    contribution = data["groups"][key]["contribution"]
    members = data["groups"][key]["members"]
    writer.write(f'\n\n')
    writer.write(f'**{key}:** {contact}\n\n')
    writer.write(f'*{contribution}*\n\n')

    for name in members:
        writer.write(f'- {name}\n')


def writeGroupMarkdown(data, key):
    contact = data["groups"][key]["contact"]
    contribution = data["groups"][key]["contribution"]
    members = data["groups"][key]["members"]

    writer.write(f'\n\n')
    writer.write(f'**{key}:** {contact}\n\n')
    writer.write(f'*{contribution}*\n\n')

    for name in members:
        writer.write(f'- {name}\n')

    writer.write(f'\n\n')

    #write.write("%s" data["groups"][key]["contribution"])
    #writer.write('## %s, %s\n'%(key,
    #                            data["groups"][key]["contact"]))


infile = 'summary.yaml'
with open(infile, "r") as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

outfile = 'groups.rst'
with open(outfile, 'w') as writer:
    #writer.write('# Summary of SIT-Com In-kind Contributions\n')

    writer.write('International In-Kind Contribution Program\n')
    writer.write('------------------------------------------\n')

    for key in data["groups"].keys():
        if "US/Chile" not in key:
            writeGroup(data, key)

    writer.write('\n\n')
    writer.write('US/Chile Community Engagement with Rubin Observatory Commissioning Effort Program\n')
    writer.write('---------------------------------------------------------------------------------\n')

    for key in data["groups"].keys():
        if "US/Chile" in key:
            writeGroup(data, key)

"""
outfile = 'summary.md'
with open(outfile, 'w') as writer:
    writer.write('# Summary of SIT-Com In-kind Contributions\n')

    for key in data["groups"].keys():
        writeGroup(data, key)
"""
