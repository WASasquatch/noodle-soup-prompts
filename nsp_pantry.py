import random, json, subprocess, os

nspterminology = None

def wget(url, output):
    res = subprocess.run(['wget', '-q', '--show-progress', url, '-O', output], stdout=subprocess.PIPE).stdout.decode('utf-8')
    print(res)

# nsp_parse( prompt )
# Input: dict, list, str
# Parse strings for terminology keys and replace them with random terms
def nsp_parse(prompt):

    global nspterminology
	
    new_prompt = ''
    new_prompts = []
    new_dict = {}
    ptype = type(prompt)
	
    if not os.path.exists('./nsp_pantry.json'):
        wget('https://raw.githubusercontent.com/WASasquatch/noodle-soup-prompts/main/nsp_pantry.json', './nsp_pantry.json')
	
    nspterminology = json.load('./nsp_pantry.json')

    if ptype == dict:
        for pstep, pvalue in prompt.items():
            if type(pvalue) == list:
                for prompt in pvalue:
                    new_prompt = prompt
                    for term in nspterminology:
                        tkey = f'_{term}_'
                        tcount = prompt.count(tkey)
                        for i in range(tcount):
                            new_prompt = new_prompt.replace(tkey, random.choice(nspterminology[term]), 1)
                    new_prompts.append(new_prompt)
                new_dict[pstep] = new_prompts
                new_prompts = []
        return new_dict
    elif ptype == list:
        for pstr in prompt:
            new_prompt = pstr
            for term in nspterminology:
                tkey = f'_{term}_'
                tcount = new_prompt.count(tkey)
                for i in range(tcount):
                    new_prompt = new_prompt.replace(tkey, random.choice(nspterminology[term]), 1)
            new_prompts.append(new_prompt)
            new_prompt = None
        return new_prompts
    elif ptype == str:
        new_prompt = prompt
        for term in nspterminology:
            tkey = f'_{term}_'
            tcount = new_prompt.count(tkey)
            for i in range(tcount):
                new_prompt = new_prompt.replace(tkey, random.choice(nspterminology[term]), 1)
        return new_prompt
    else:
        return 
