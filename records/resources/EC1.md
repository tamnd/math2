---
records:
    - id: EC1VHMV3RS
      kind: monograph
      title: 'Probability Theory: A Comprehensive Course'
      creators:
        - name: Achim Klenke
          role: author
      date: "2014"
      expressions:
        - key: e1
          kind: edition
          date: "2014"
          ids:
            doi:
                - 10.1007/978-1-4471-5361-0
                - 10.1007/978-3-030-56402-5
          manifestations:
            - key: m1
              kind: print
              publisher: Springer London
              date: "2014"
              ids:
                isbn:
                    - "9781447153603"
                    - "9781447153610"
            - key: m2
              kind: print
              publisher: Springer International Publishing
              date: "2020"
              ids:
                isbn:
                    - "9783030564018"
                    - "9783030564025"
      relations:
        - kind: part_of
          to: W0CC03QJC7
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4471-5361-0
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-030-56402-5
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
