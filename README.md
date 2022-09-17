# **Noodle Soup Prompts** - Prompt Terminology Generator</font> ![visitors](https://visitor-badge.glitch.me/badge?page_id=Noodle-Soup-Prompts-Github&left_color=blue&right_color=orange) 

<a href="https://rebrand.ly/noodle-soup-prompts"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

&nbsp;

This tool contains a *growing* database of terminology to help build interesting prompts for [Disco Diffusion](https://discodiffusion.com/). **Give it a try!**

Artist names gathered by **MisterRuffian** (Discord Misterruffian#2891) on his amazing [Latent Artist & Modifier Encyclopedia](https://docs.google.com/spreadsheets/d/1_jgQ9SyvUaBNP1mHHEzZ6HhL_Es1KwBKQtnpnmWW82I/).

Terminology Database created by **WAS**asquatch (Discord: WAS\#0263)

# Contribute
Feel free to make pull requests with new terminology. Let's make this a expansive and easy way to discover new prompts!

# Installation

#### **Update**: You do not use `import nspterminology` anymore. NSP will download the terminology database json on first run. 

Noodle Soup Prompts was initially meant to be just a basic script for random prompt generation, but I have moved things over to a PY file you can download and import to use the database in your own projects. 


## Download `nsp_pantry.py` (Python)
```
wget -q --show-progress --no-cache 'https://raw.githubusercontent.com/WASasquatch/noodle-soup-prompts/main/nsp_pantry.py'
```

## Download `nsp_pantry.json` (JSON)
```
wget -q --show-progress --no-cache 'https://raw.githubusercontent.com/WASasquatch/noodle-soup-prompts/main/nsp_pantry.json'
```

## Import and Parse (Python)

```python
import nsp_pantry
from nsp_pantry import nsp_parse

text_prompts = {
    0: [
        "Portrait of a _adj-beauty_ _noun-emote_ _nationality_ woman with pearlescent skin and white hair by _artist_, _site_.:5",
        "_hd_, _hd_, _3d-terms_, _3d-terms_:2",
        "_color_ Color Scheme",
        ],
}

new_prompts = nsp_parse(text_prompts)

print(new_prompts)
```
**Note:** `nsp_parse()` can accept `dict`, `list` and `str` input. 


### Example Output
```python
{0: ['Portrait of a goodly Enraged Hungarian woman with pearlescent skin and white hair by Ferdinand Keller, trending on CGSociety.:5', 'HDR, 12k resolution, Bitmap, Raster graphics:2', 'Uranian blue Color Scheme']}
```



