---
records:
    - id: XH1JZJK3F7
      kind: monograph
      title: Fibre Bundles
      creators:
        - name: Dale Husemoller
          role: author
      date: "1966"
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1966"
          ids:
            doi:
                - 10.1007/978-1-4757-2261-1
                - 10.1007/978-1-4757-4008-0
            zbl: "0144.44804"
            zbl_id: "3233464"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1994"
              ids:
                isbn:
                    - "9781475722635"
                    - "9781475722611"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1966"
              ids:
                isbn:
                    - "9781475740103"
                    - "9781475740080"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-2261-1
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-4008-0
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "3233464"
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
