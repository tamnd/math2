---
records:
    - id: SEDFWK2VJ6
      kind: monograph
      title: p-adic Numbers, p-adic Analysis, and Zeta-Functions
      creators:
        - name: Neal Koblitz
          role: author
      date: "1977"
      expressions:
        - key: e1
          kind: edition
          date: "1977"
          ids:
            doi:
                - 10.1007/978-1-4612-1112-9
                - 10.1007/978-1-4684-0047-2
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1984"
              ids:
                isbn:
                    - "9781461270140"
                    - "9781461211129"
            - key: m2
              kind: print
              publisher: Springer US
              date: "1977"
              ids:
                isbn:
                    - "9781468400496"
                    - "9781468400472"
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-1112-9
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-0047-2
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
