---
records:
    - id: KET4ZJ4S5P
      kind: monograph
      title: Shapes and Diffeomorphisms
      creators:
        - name: Laurent Younes
          role: author
          ids:
            orcid: 0000-0003-2017-9565
      date: "2010"
      expressions:
        - key: e1
          kind: edition
          date: "2010"
          ids:
            doi:
                - 10.1007/978-3-642-12055-8
                - 10.1007/978-3-662-58496-5
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2010"
              ids:
                isbn:
                    - "9783642120541"
                    - "9783642120558"
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2019"
              ids:
                isbn:
                    - "9783662584958"
                    - "9783662584965"
      relations:
        - kind: part_of
          to: 2M0N86YNGA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-642-12055-8
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-58496-5
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
