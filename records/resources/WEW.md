---
records:
    - id: WEWNQ5P2FA
      kind: monograph
      title: Fourier Series
      creators:
        - name: R. E. Edwards
          role: author
      date: "1979"
      msc:
        - code: 42-02
          from: zbmath_search
        - code: 42A20
          from: zbmath_search
        - code: 42A24
          from: zbmath_search
        - code: 42A85
          from: zbmath_search
        - code: 40G05
          from: zbmath_search
        - code: 43-02
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          label: 2nd edition
          language: en
          date: "1979"
          ids:
            doi:
                - 10.1007/978-1-4612-6208-4
                - 10.1007/978-1-4613-8156-3
            zbl: "0424.42001"
            zbl_id: "3660183"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1979"
              ids:
                isbn:
                    - "9781461262107"
                    - "9781461262084"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1982"
              ids:
                isbn:
                    - "9781461381587"
                    - "9781461381563"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-6208-4
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4613-8156-3
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "3660183"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
