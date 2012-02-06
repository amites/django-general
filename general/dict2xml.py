from general.utils_dict import dict2xml

if __name__ == '__main__':
    structure = {
        'sibbling' : {
            'grandPa' : {
                'dad' : {
                    'name' : 'foo',
                    'childs' : {
                        'child' :
                            ['me', 'bro', ],
                    },
                },
                'uncle' : 'bar',
            },
        },
    }
    xml = dict2xml(structure)
    xml.display()