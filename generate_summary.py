import yaml

def writeGroupRST(data, key):
    contact = data["groups"][key]["contact"]
    contribution = data["groups"][key]["contribution"]
    members = data["groups"][key]["members"]

    writer.write(f'\n\n')
    writer.write(f'**{key}:** *{contribution}*\n\n')
    writer.write(f'  Point of Contact: {contact}\n\n')
    writer.write('  Members: ' + ', '.join(members) + '\n')

    """
    writer.write(f'\n\n')
    writer.write(f'**{key}:** {contact} (Point of Contact)\n\n')
    writer.write(f'  Contribution: *{contribution}*\n\n')

    #for name in members:
    #    writer.write(f'- {name}\n')
    writer.write("  Members: " + ", ".join(members) + '\n')
    """


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
    writer.write('.. Do NOT modify this file directly; edit summary.yaml instead.\n\n')

    writer.write('International In-Kind Contribution Program\n')
    writer.write('------------------------------------------\n')

    for key in data["groups"].keys():
        if "US/Chile" not in key and "University" not in key:
            writeGroupRST(data, key)

    writer.write('\n\n')
    writer.write('US/Chile Community Engagement with Rubin Observatory Commissioning Effort Program\n')
    writer.write('---------------------------------------------------------------------------------\n')

    for key in data["groups"].keys():
        if "US/Chile" in key and "University" not in key:
            writeGroupRST(data, key)

    writer.write('\n\n')
    writer.write('.. _institutional_contributions:\n')
    writer.write('\n\n')
    writer.write('Institutional Contributions to Rubin Observatory Construction\n')
    writer.write('-------------------------------------------------------------\n')

    for key in data["groups"].keys():
        if "University" in key and "US/Chile" not in key:
            writeGroupRST(data, key)

"""
outfile = 'summary.md'
with open(outfile, 'w') as writer:
    writer.write('# Summary of SIT-Com In-kind Contributions\n')

    for key in data["groups"].keys():
        writeGroup(data, key)
"""
