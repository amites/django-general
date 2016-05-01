from copy import deepcopy

from xml.dom.minidom import Document


class dict2xml(object):
    doc = Document()

    def __init__(self, structure):
        if len(structure) == 1:
            rootName = str(structure.keys()[0])
            self.root = self.doc.createElement(rootName)
            self.doc.appendChild(self.root)
            self.build(self.root, structure[rootName])

    def display(self):
        print self.doc.toprettyxml(indent=" ")

    def build(self, father, structure):
        if type(structure) == dict:
            tag = ''
            k = ''
            for k in structure:
                tag = self.doc.createElement(k)
            father.appendChild(tag)
            self.build(tag, structure[k])

        elif type(structure) == list:
            grandFather = father.parentNode
            uncle = deepcopy(father)
            for l in structure:
                self.build(father, l)
                grandFather.appendChild(father)
                father = deepcopy(uncle)

        else:
            data = str(structure)
            tag = self.doc.createTextNode(data)
            father.appendChild(tag)


def clearEmpties(d):
    """
    Removes empty values from a dict.
    """
    v = None
    try:
        return dict([(k, v) for k, v in d.items() if v and len(str(v)) > 0])
    except TypeError:
        print 'Failed to clearEmpties: for value: {}'.format(v)


if __name__ == '__main__':
    struct = {
        'sibbling': {
            'grandPa': {
                'dad': {
                    'name': 'foo',
                    'childs': {
                        'child':
                            ['me', 'bro', ],
                    },
                },
                'uncle': 'bar',
            },
        },
    }
    xml = dict2xml(struct)
    xml.display()
