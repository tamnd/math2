---
records:
    - id: TST01PDXSV
      kind: monograph
      title: Abstract Harmonic Analysis
      creators:
        - name: Edwin Hewitt
          role: author
        - name: Kenneth A. Ross
          role: author
      date: "1970"
      expressions:
        - key: e1
          kind: edition
          date: "1970"
          ids:
            doi:
                - 10.1007/978-1-4419-8638-2
                - 10.1007/978-3-642-62008-9
                - 10.1007/978-3-662-26755-4
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1979"
              ids:
                isbn:
                    - "9780387941905"
                    - "9781441986382"
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1970"
              ids:
                isbn:
                    - "9783540583189"
                    - "9783642620089"
            - key: m3
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1970"
              ids:
                isbn:
                    - "9783662245958"
                    - "9783662267554"
      relations:
        - kind: part_of
          to: GQFCNY816R
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4419-8638-2
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-642-62008-9
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-26755-4
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
