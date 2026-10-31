---
records:
    - id: DFB60V71TW
      kind: monograph
      title: Topological Methods in Hydrodynamics
      creators:
        - name: Vladimir I. Arnold
          role: author
        - name: Boris A. Khesin
          role: author
      date: "1998"
      expressions:
        - key: e1
          kind: edition
          date: "1998"
          ids:
            doi:
                - 10.1007/978-3-030-74278-2
                - 10.1007/b97593
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2021"
              ids:
                isbn:
                    - "9783030742775"
                    - "9783030742782"
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1998"
              ids:
                isbn:
                    - "9780387949475"
                    - "9780387225890"
      relations:
        - kind: part_of
          to: 2M0N86YNGA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-030-74278-2
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/b97593
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
