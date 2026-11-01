---
records:
    - id: XHQGQT5P60
      kind: monograph
      title: Undergraduate Algebra
      creators:
        - name: Serge Lang
          role: author
      date: "1987"
      msc:
        - code: 00-01
          from: zbmath_search
        - code: 13-01
          from: zbmath_search
        - code: 12-01
          from: zbmath_search
        - code: 20-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1987"
          ids:
            doi:
                - 10.1007/978-1-4684-9234-7
                - 10.1007/978-1-4757-6898-5
            zbl: "0627.00002"
            zbl_id: "4018948"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1987"
              ids:
                isbn:
                    - "9781468492361"
                    - "9781468492347"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1990"
              ids:
                isbn:
                    - "9781475769005"
                    - "9781475768985"
              access:
                class: record
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-9234-7
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-6898-5
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "4018948"
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
