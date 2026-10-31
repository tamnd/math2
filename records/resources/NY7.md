---
records:
    - id: NY7V3SM38K
      kind: monograph
      title: Dynamical Systems VII
      creators:
        - name: V. I. Arnol’d
          role: editor
        - name: S. P. Novikov
          role: editor
      date: "1993"
      expressions:
        - key: e1
          kind: edition
          date: "1993"
          ids:
            doi:
                - 10.1007/978-3-662-06796-3
                - 10.1007/978-3-662-06798-7
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1994"
              ids:
                isbn:
                    - "9783642057380"
                    - "9783662067963"
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1993"
              ids:
                isbn:
                    - "9783642081019"
                    - "9783662067987"
      relations:
        - kind: part_of
          to: XGZPMQ7BSM
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-06796-3
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-06798-7
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
