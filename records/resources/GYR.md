---
records:
    - id: GYREK3A0PQ
      kind: monograph
      title: 'Principal Bundles: The Classical Case'
      creators:
        - name: Stephen Bruce Sontz
          role: author
      date: "2015"
      expressions:
        - key: e1
          kind: edition
          date: "2015"
          ids:
            doi:
                - 10.1007/978-3-319-14765-9
                - 10.1007/978-3-319-15829-7
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2015"
              ids:
                isbn:
                    - "9783319147642"
                    - "9783319147659"
            - key: m2
              kind: print
              publisher: Springer International Publishing
              date: "2015"
              ids:
                isbn:
                    - "9783319158280"
                    - "9783319158297"
      relations:
        - kind: part_of
          to: W0CC03QJC7
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-14765-9
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-15829-7
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
