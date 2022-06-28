import copy

import jupytext
import nbconvert
import nbformat


def drop_untagged(nbook, tags, drop_tags=[]):
    outbook = copy.deepcopy(nbook)
    for cell in nbook["cells"]:
        metadata = cell["metadata"] or dict()
        drop = False
        for tag in tags:
            if tag not in metadata.get("tags", [tag]):
                drop = True
                break
        for tag in drop_tags:
            if tag in metadata.get("tags", [tag]):
                drop = True
                break
        if drop:
            outbook["cells"].remove(cell)
    return outbook


nbook = jupytext.read("setup.md", fmt="md:myst")
nbformat.write(nbook, "setup.ipynb")
config = {'TemplateExporter': {'exclude_input_prompt': True,
                               'exclude_output_prompt': True}}
html_exporter = nbconvert.get_exporter('html', config=config)
script_exporter = nbconvert.get_exporter('script', config=config)
for tag in ("mac", "windows"):
    versioned_nbook = drop_untagged(nbook, [tag])
    html_output = nbconvert.export(html_exporter,
                                   versioned_nbook)
    with open(f"html/{tag}_setup.html", "w") as outfile:
        outfile.write(html_output[0])
        versioned_nbook = drop_untagged(nbook, [tag], ["noscript"])
    script_output = nbconvert.export(script_exporter,
                                     versioned_nbook)
    with open(f"scripts/{tag}_setup.sh", "w") as outfile:
        outfile.write(script_output[0])
