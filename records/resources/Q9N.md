---
records:
    - id: Q9N5HWNM1R
      kind: monograph
      title: Introduction to Coding Theory
      creators:
        - name: J. H. van Lint
          role: author
      date: "1982"
      msc:
        - code: 94B05
          from: zbmath_search
        - code: 94-01
          from: zbmath_search
        - code: 94B15
          from: zbmath_search
        - code: 94B10
          from: zbmath_search
        - code: 94B40
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1982"
          ids:
            doi:
                - 10.1007/978-3-642-58575-3
                - 10.1007/978-3-662-00174-5
                - 10.1007/978-3-662-07998-0
            zbl: "0485.94015"
            zbl_id: "3763833"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1999"
              ids:
                isbn:
                    - "9783642636530"
                    - "9783642585753"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1992"
              ids:
                isbn:
                    - "9783662001769"
                    - "9783662001745"
              access:
                class: record
            - key: m3
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1982"
              ids:
                isbn:
                    - "9783662080009"
                    - "9783662079980"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 dev scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-642-58575-3
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-00174-5
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-07998-0
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "3763833"
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
