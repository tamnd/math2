---
records:
    - id: EXFB1SNYPD
      kind: monograph
      title: 'Probability-1: Volume 1'
      creators:
        - name: Albert N. Shiryaev
          role: author
      date: "2016"
      expressions:
        - key: e1
          kind: edition
          date: "2016"
          ids:
            doi: 10.1007/978-0-387-72206-1
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2016"
              ids:
                isbn:
                    - "9780387722054"
                    - "9780387722061"
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-0-387-72206-1
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
