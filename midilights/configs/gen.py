#!/usr/bin/env python3

key_begin = 36
key_end = 84
output_begin = 0
output_end = 48

def write_mapping(file, i, in_keys, out_keys):
    in_keys_str = ','.join(in_keys)
    out_keys_str = ','.join(out_keys)
    output = '''    {
      "inputkeys": [
        ''' + in_keys_str + '''
      ],
      "outputchannels": [
        ''' + out_keys_str + '''
      ]
    }'''
    if i == 0:
        file.write(output)
    else:
        file.write(',\n' + output)


with open('gen_mapping.json', 'w') as file:
    file.write('''
{
  "keybegin": 36,
  "keyend": 84,
  "outputbegin": 0,
  "outputend": 48,
  "mappings": [
''')

    for i in range(12):
        input_keys = []
        for octave in range(4):
            input_keys.append(str(octave * 12 + i + key_begin))
        output_keys = [str(i + output_begin)]
        write_mapping(file, i, input_keys, output_keys)

    file.write('''
  ]
}''')

