---
records:
    - id: QWBSYY1MP8
      kind: monograph
      title: Measure and Category
      creators:
        - name: John C. Oxtoby
          role: author
      date: "1971"
      msc:
        - code: 28-02
          from: zbmath_search
        - code: 28Axx
          from: zbmath_search
        - code: 18B05
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1971"
          ids:
            doi:
                - 10.1007/978-1-4615-9964-7
                - 10.1007/978-1-4684-9339-9
            zbl: "0217.09201"
            zbl_id: "3344793"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer US
              date: "1971"
              ids:
                isbn:
                    - "9780387053493"
                    - "9781461599647"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1980"
              ids:
                isbn:
                    - "9781468493412"
                    - "9781468493399"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4615-9964-7
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-9339-9
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "3344793"
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
