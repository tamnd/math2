---
records:
    - id: YX8QHVWV1B
      kind: monograph
      title: An Outline of Set Theory
      creators:
        - name: James M. Henle
          role: author
      date: "1986"
      msc:
        - code: 03-01
          from: zbmath_search
        - code: "03E20"
          from: zbmath_search
        - code: 00A07
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1986"
          ids:
            doi: 10.1007/978-1-4613-8680-3
            zbl: "0613.04001"
            zbl_id: "3991501"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1986"
              ids:
                isbn:
                    - "9780387963686"
                    - "9781461386803"
              access:
                class: record
      relations:
        - kind: part_of
          to: AQAR17SPHM
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4613-8680-3
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "3991501"
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
