---
records:
    - id: Y1EEB7KZ2H
      kind: monograph
      title: Essentials of Integration Theory for Analysis
      creators:
        - name: Daniel W. Stroock
          role: author
      date: "2011"
      expressions:
        - key: e1
          kind: edition
          date: "2011"
          ids:
            doi:
                - 10.1007/978-1-4614-1135-2
                - 10.1007/978-3-030-58478-8
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2011"
              ids:
                isbn:
                    - "9781461411345"
                    - "9781461411352"
            - key: m2
              kind: print
              publisher: Springer International Publishing
              date: "2020"
              ids:
                isbn:
                    - "9783030584771"
                    - "9783030584788"
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4614-1135-2
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-030-58478-8
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
