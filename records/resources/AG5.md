---
records:
    - id: AG5F5Z4YCW
      kind: monograph
      title: Introduction to Linear Algebra
      creators:
        - name: Serge Lang
          role: author
      date: "1986"
      msc:
        - code: 15-01
          from: zbmath_search
        - code: 65F05
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          label: 2nd edition
          language: en
          date: "1986"
          ids:
            doi: 10.1007/978-1-4612-1070-2
            zbl: "0577.15001"
            zbl_id: "3922866"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1986"
              ids:
                isbn:
                    - "9781461270027"
                    - "9781461210702"
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
          native_id: 10.1007/978-1-4612-1070-2
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "3922866"
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
