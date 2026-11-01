---
records:
    - id: WSPX1PR8R2
      kind: monograph
      title: 'Partial Differential Equations: An Introduction to Analytical and Numerical Methods'
      creators:
        - name: Wolfgang Arendt
          role: author
        - name: Karsten Urban
          role: author
      date: "2023"
      msc:
        - code: 35-01
          from: zbmath_search
        - code: 65-01
          from: zbmath_search
        - code: 35Cxx
          from: zbmath_search
        - code: 65Mxx
          from: zbmath_search
        - code: 65Nxx
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2023"
          ids:
            doi: 10.1007/978-3-031-13379-4
            zbl: "1507.35001"
            zbl_id: "7581830"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2023"
              ids:
                isbn:
                    - "9783031133787"
                    - "9783031133794"
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
          native_id: 10.1007/978-3-031-13379-4
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "7581830"
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
