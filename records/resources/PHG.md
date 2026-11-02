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
        - code: 60-06
          from: zbmath_search
        - code: 00B25
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2008"
          ids:
            doi:
                - 10.1007/978-3-540-77913-1
                - 10.1007/978-3-642-01763-6
            zbl: "1140.60002"
            zbl_id: "5281908"
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
        rule: S1
        by: m2 dev scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-540-77913-1
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-642-01763-6
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "5281908"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-02"
          by: m2 dev scope/1
          note: from in to in
---
