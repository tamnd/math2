---
records:
    - id: PHNY20PP0J
      kind: monograph
      title: Applied Abstract Algebra
      creators:
        - name: Rudolf Lidl
          role: author
        - name: Günter Pilz
          role: author
      date: "1984"
      expressions:
        - key: e1
          kind: edition
          date: "1984"
          ids:
            doi:
                - 10.1007/978-1-4615-6465-2
                - 10.1007/978-1-4757-2941-2
          manifestations:
            - key: m1
              kind: print
              publisher: Springer US
              date: "1984"
              ids:
                isbn:
                    - "9780387961668"
                    - "9781461564652"
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1998"
              ids:
                isbn:
                    - "9781441931177"
                    - "9781475729412"
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4615-6465-2
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-2941-2
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
