---
records:
    - id: VX52BJ1X4H
      kind: monograph
      title: Inverse Galois Theory
      creators:
        - name: Gunter Malle
          role: author
        - name: B. Heinrich Matzat
          role: author
      date: "1999"
      msc:
        - code: 12F12
          from: zbmath_search
        - code: 12-02
          from: zbmath_search
        - code: 12F10
          from: zbmath_search
        - code: 12G05
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1999"
          ids:
            doi:
                - 10.1007/978-3-662-12123-8
                - 10.1007/978-3-662-55420-3
            zbl: "0940.12001"
            zbl_id: "1341901"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1999"
              ids:
                isbn:
                    - "9783642083112"
                    - "9783662121238"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2018"
              ids:
                isbn:
                    - "9783662554197"
                    - "9783662554203"
              access:
                class: record
      relations:
        - kind: part_of
          to: FA5PXCH6G7
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-12123-8
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-55420-3
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "1341901"
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
