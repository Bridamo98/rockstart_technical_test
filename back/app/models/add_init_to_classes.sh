#!/bin/bash

archivo="$1"

if [[ ! -f "$archivo" ]]; then
    echo "El archivo $archivo no existe. Por favor, proporciona un archivo válido."
    exit 1
fi

awk '
BEGIN {
    in_class = 0
    field_index = 0
}

/^\s*class [A-Za-z_][A-Za-z0-9_]*\(Base\):/ {
    in_class = 1
    printed_create = 0
    field_index = 0
    delete fields_list
    delete field_order
    print
    next
}

/^    __tablename__/ && in_class {
    print
    print "    def __init__(self):"
    print "        # Intentional empty constructor due this code is generated automatically"
    print "        pass"
    next
}

/^    [a-zA-Z_][a-zA-Z0-9_]*: Mapped\[.*\] = mapped_column/ && in_class {
    match($0, /^\s*([a-zA-Z_][a-zA-Z0-9_]*): Mapped\[(Optional\[[^]]+\]|[^]]+)\]/, m)
    if ($0 ~ /primary_key=True/) {
        print
        next
    }
    if (m[1] != "" && m[2] != "") {
        fields_list[m[1]] = m[2]
        field_order[++field_index] = m[1]
    }
    print
    next
}

/^    relationship/ && in_class {
    print
    next
}

/^$/ && in_class && field_index > 0 && !printed_create {
    printed_create = 1
    print ""
    print "    @classmethod"
    printf("    def create(cls")
    for (i = 1; i <= field_index; i++) {
        name = field_order[i]
        type = fields_list[name]
        # si es Optional[...] le asignamos =None por defecto
        if (type ~ /^Optional\[/) {
            printf(", %s: %s = None", name, type)
        } else {
            printf(", %s: %s", name, type)
        }
    }
    print "):"
    print "        obj = cls()"
    for (i = 1; i <= field_index; i++) {
        name = field_order[i]
        print "        obj." name " = " name
    }
    print "        return obj"
    next
}

/^\s*$/ {
    if (in_class && printed_create) {
        in_class = 0
    }
    print
    next
}

{ print }
' "$archivo" > "${archivo}.tmp" && mv "${archivo}.tmp" "$archivo"

echo "El archivo ha sido modificado correctamente."
