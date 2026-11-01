---
records:
    - id: PHG1G06NHV
      kind: monograph
      title: Séminaire de Probabilités XLI
      creators:
        - name: Catherine Donati-Martin
          role: editor
        - name: Michel Émery
          role: editor
        - name: Alain Rouault
          role: editor
        - name: Christophe Stricker
          role: editor
      date: "2008"
      msc:
        - code: 00-XX
          from: classify/1@2b838f8bc9d8
      expressions:
        - key: e1
          kind: edition
          date: "2008"
          ids:
            doi:
                - 10.1007/978-3-540-77913-1
                - 10.1007/978-3-642-01763-6
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2008"
              ids:
                isbn:
                    - "9783540779124"
                    - "9783540779131"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2009"
              ids:
                isbn:
                    - "9783642017629"
                    - "9783642017636"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-540-77913-1
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-642-01763-6
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
