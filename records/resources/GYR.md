---
records:
    - id: GYREK3A0PQ
      kind: monograph
      title: 'Principal Bundles: The Classical Case'
      creators:
        - name: Stephen Bruce Sontz
          role: author
      date: "2015"
      msc:
        - code: 53-01
          from: zbmath_search
        - code: 53C20
          from: zbmath_search
        - code: 53C05
          from: zbmath_search
        - code: 53C07
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2015"
          ids:
            doi:
                - 10.1007/978-3-319-14765-9
                - 10.1007/978-3-319-15829-7
            zbl: "1321.53004"
            zbl_id: "6401002"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2015"
              ids:
                isbn:
                    - "9783319147642"
                    - "9783319147659"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer International Publishing
              date: "2015"
              ids:
                isbn:
                    - "9783319158280"
                    - "9783319158297"
              access:
                class: record
      relations:
        - kind: part_of
          to: W0CC03QJC7
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-14765-9
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-15829-7
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "6401002"
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
