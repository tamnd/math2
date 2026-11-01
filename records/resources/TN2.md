---
records:
    - id: TN2R331FKS
      kind: monograph
      title: A Formal Background to Mathematics
      creators:
        - name: Robert Edwards
          role: author
      date: "1979"
      msc:
        - code: 03-01
          from: zbmath_search
        - code: 06-01
          from: zbmath_search
        - code: 08-01
          from: zbmath_search
        - code: 00A05
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1979"
          ids:
            doi:
                - 10.1007/978-1-4612-9984-4
                - 10.1007/978-1-4613-8096-2
            zbl: "0413.03001"
            zbl_id: "3641401"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1979"
              ids:
                isbn:
                    - "9780387904313"
                    - "9781461299844"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1980"
              ids:
                isbn:
                    - "9780387905136"
                    - "9781461380962"
              access:
                class: record
      relations:
        - kind: part_of
          to: W0CC03QJC7
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-9984-4
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4613-8096-2
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3641401"
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
