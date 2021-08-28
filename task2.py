import yaml
import os

d = {'my_project':
    [{'settings': [
        '__init__.py', 'dev.py', 'prod.py'
    ],
    },
        {'mainapp': [
            '__init__.py', 'models.py', 'views.py', {'templates': [{
                'mainapp': ['base.html', 'index.html']}]
            }]},
        {'authapp': ['__init__.py', 'models.py', 'views.py', {'templates': [{
            'authapp': ['base.html', 'index.html']}]
        }
                     ]
         }
    ]
}
f = open('config.yaml', 'w')
f.write(yaml.dump(d))
f.close()

with open("config.yaml") as y_file:
    d = yaml.safe_load(y_file)


def create_data(data):
   for folder, data_temps in data.items():
       if not os.path.exists(folder):
           os.mkdir(folder)
       os.chdir(folder)
       for data_temp in data_temps:
           if isinstance(data_temp, dict):
               create_data(data_temp)
           else:
               if os.path.exists(data_temp):
                   if '.' in data_temp:
                       with open(data_temp, 'w') as f:
                           f.write('')
   else:
       os.chdir('../')

create_data(d)



