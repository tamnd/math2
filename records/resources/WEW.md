---
records:
    - id: WEWNQ5P2FA
      kind: monograph
      title: Fourier Series
      creators:
        - name: R. E. Edwards
          role: author
      date: "1979"
      expressions:
        - key: e1
          kind: edition
          date: "1979"
          ids:
            doi:
                - 10.1007/978-1-4612-6208-4
                - 10.1007/978-1-4613-8156-3
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1979"
              ids:
                isbn:
                    - "9781461262107"
                    - "9781461262084"
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1982"
              ids:
                isbn:
                    - "9781461381587"
                    - "9781461381563"
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
          native_id: 10.1007/978-1-4612-6208-4
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4613-8156-3
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
