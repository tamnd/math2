---
records:
    - id: CDV146A8T4
      kind: monograph
      title: Coding Theory
      creators:
        - name: Jacobus H. van Lint
          role: author
      date: "1971"
      expressions:
        - key: e1
          kind: edition
          date: "1971"
          ids:
            doi:
                - 10.1007/978-3-540-36657-7
                - 10.1007/978-3-662-20712-3
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1973"
              ids:
                isbn:
                    - "9783540063636"
                    - "9783540366577"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1971"
              ids:
                isbn:
                    - "9783540054764"
                    - "9783662207123"
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
          native_id: 10.1007/978-3-540-36657-7
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-20712-3
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
