---
records:
    - id: DJZP8A5MF9
      kind: monograph
      title: Complex Analysis
      creators:
        - name: Serge Lang
          role: author
      date: "1985"
      msc:
        - code: 30-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          label: 2nd edition
          language: en
          date: "1985"
          ids:
            doi:
                - 10.1007/978-1-4757-1871-3
                - 10.1007/978-1-4757-3083-8
                - 10.1007/978-3-642-59273-7
            zbl: "0562.30001"
            zbl_id: "3895331"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1985"
              ids:
                isbn:
                    - "9781475718737"
                    - "9781475718713"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1999"
              ids:
                isbn:
                    - "9781441931351"
                    - "9781475730838"
              access:
                class: record
            - key: m3
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1993"
              ids:
                isbn:
                    - "9783540780595"
                    - "9783642592737"
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
          native_id: 10.1007/978-1-4757-1871-3
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-3083-8
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-642-59273-7
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "3895331"
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
