---
records:
    - id: DWF2JGHGAE
      kind: monograph
      title: The Radon Transform
      creators:
        - name: Sigurdur Helgason
          role: author
      date: "1980"
      expressions:
        - key: e1
          kind: edition
          date: "1980"
          ids:
            doi:
                - 10.1007/978-1-4757-1463-0
                - 10.1007/978-1-4899-6765-7
          manifestations:
            - key: m1
              kind: print
              publisher: Springer US
              date: "1999"
              ids:
                isbn:
                    - "9781475714654"
                    - "9781475714630"
            - key: m2
              kind: print
              publisher: Birkhäuser Boston
              date: "1980"
              ids:
                isbn:
                    - "9781489967671"
                    - "9781489967657"
      relations:
        - kind: part_of
          to: VS2PFDMCR5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-1463-0
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4899-6765-7
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
