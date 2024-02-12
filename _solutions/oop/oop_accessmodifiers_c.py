
public = {attrname: attrvalue
          for attrname, attrvalue in vars(DATA).items()
          if not attrname.startswith('_')}

protected = {attrname: attrvalue
             for attrname, attrvalue in vars(DATA).items()
             if attrname.startswith('_')
             and not attrname.startswith(f'_User__')}

private = {attrname: attrvalue
           for attrname, attrvalue in vars(DATA).items()
           if attrname.startswith(f'_User__')}
